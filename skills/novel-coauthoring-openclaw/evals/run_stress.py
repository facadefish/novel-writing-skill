import json
import statistics
import sys
from pathlib import Path


def percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = (len(ordered) - 1) * q
    low = int(idx)
    high = min(low + 1, len(ordered) - 1)
    frac = idx - low
    return ordered[low] * (1 - frac) + ordered[high] * frac


def load_template(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    goals = {}
    for line in lines:
        t = line.strip()
        if t.startswith("p95_latency_ms:"):
            goals["p95_latency_ms"] = float(t.split(":")[1].strip())
        if t.startswith("avg_prompt_tokens:"):
            goals["avg_prompt_tokens"] = float(t.split(":")[1].strip())
        if t.startswith("avg_completion_tokens:"):
            goals["avg_completion_tokens"] = float(t.split(":")[1].strip())
    return goals


def load_metrics(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s:
            continue
        rows.append(json.loads(s))
    return rows


def summarize(rows: list[dict]) -> dict:
    latency = [float(r["latency_ms"]) for r in rows]
    prompt = [float(r["prompt_tokens"]) for r in rows]
    completion = [float(r["completion_tokens"]) for r in rows]
    alerts = [1.0 for r in rows if bool(r.get("alert"))]
    return {
        "samples": len(rows),
        "p50_latency_ms": round(percentile(latency, 0.50), 2),
        "p95_latency_ms": round(percentile(latency, 0.95), 2),
        "p99_latency_ms": round(percentile(latency, 0.99), 2),
        "avg_prompt_tokens": round(statistics.fmean(prompt), 2),
        "avg_completion_tokens": round(statistics.fmean(completion), 2),
        "alert_rate": round((len(alerts) / len(rows)) if rows else 0.0, 4),
    }


def evaluate(summary: dict, goals: dict) -> dict:
    return {
        "p95_latency_ms_ok": summary["p95_latency_ms"] <= goals["p95_latency_ms"],
        "avg_prompt_tokens_ok": summary["avg_prompt_tokens"] <= goals["avg_prompt_tokens"],
        "avg_completion_tokens_ok": summary["avg_completion_tokens"] <= goals["avg_completion_tokens"],
    }


def write_report(path: Path, summary: dict, checks: dict) -> None:
    status = "通过" if all(checks.values()) else "未通过"
    content = "\n".join(
        [
            "# 多书并行压测基线 v1",
            "",
            "## 实测汇总",
            f"- samples: {summary['samples']}",
            f"- p50_latency_ms: {summary['p50_latency_ms']}",
            f"- p95_latency_ms: {summary['p95_latency_ms']}",
            f"- p99_latency_ms: {summary['p99_latency_ms']}",
            f"- avg_prompt_tokens: {summary['avg_prompt_tokens']}",
            f"- avg_completion_tokens: {summary['avg_completion_tokens']}",
            f"- alert_rate: {summary['alert_rate']}",
            "",
            "## 阈值检查",
            f"- p95_latency_ms_ok: {checks['p95_latency_ms_ok']}",
            f"- avg_prompt_tokens_ok: {checks['avg_prompt_tokens_ok']}",
            f"- avg_completion_tokens_ok: {checks['avg_completion_tokens_ok']}",
            "",
            "## 结论",
            f"- 本轮多书并行压测：{status}",
        ]
    )
    path.write_text(content + "\n", encoding="utf-8")


def run(repo_root: Path) -> int:
    template_path = repo_root / "skills" / "novel-coauthoring-openclaw" / "evals" / "multi-book-stress-template.yaml"
    metrics_path = repo_root / "skills" / "novel-coauthoring-openclaw-workspace" / "iteration-4" / "perf-raw-metrics-v1.jsonl"
    report_path = repo_root / "skills" / "novel-coauthoring-openclaw-workspace" / "iteration-4" / "perf-baseline-v1.md"
    goals = load_template(template_path)
    rows = load_metrics(metrics_path)
    if not rows:
        print("[FAIL] 压测数据为空")
        return 1
    summary = summarize(rows)
    checks = evaluate(summary, goals)
    write_report(report_path, summary, checks)
    print(f"[INFO] samples={summary['samples']}")
    print(f"[INFO] report={report_path}")
    if all(checks.values()):
        print("[PASS] 压测阈值通过")
        return 0
    print("[FAIL] 压测阈值未通过")
    return 2


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[3]
    sys.exit(run(root))
