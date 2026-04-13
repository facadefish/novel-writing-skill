import json
import sys
from pathlib import Path


def load_matrix(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def must_contain(text: str, tokens: list[str]) -> list[str]:
    return [t for t in tokens if t not in text]


def has_paragraph(text: str) -> bool:
    for line in text.splitlines():
        s = line.strip()
        if len(s) >= 25 and not s.startswith("-") and not s.startswith("#") and not s[0].isdigit():
            return True
    return False


def run(repo_root: Path) -> int:
    matrix_path = repo_root / "skills" / "novel-coauthoring-openclaw" / "evals" / "executable-matrix.json"
    matrix = load_matrix(matrix_path)
    targets = {
        "contract.audit.rollback.chain": repo_root / "skills" / "novel-coauthoring-openclaw-workspace" / "iteration-4" / "eval-1-audit-rollback" / "with_skill" / "outputs" / "response.md",
        "contract.asset.consistency": repo_root / "skills" / "novel-coauthoring-openclaw-workspace" / "iteration-4" / "eval-2-multi-book-memory-switch" / "with_skill" / "outputs" / "response.md",
        "integration.openclaw.retry.idempotent": repo_root / "skills" / "novel-coauthoring-openclaw-workspace" / "iteration-4" / "eval-3-openclaw-signed-retry-metrics" / "with_skill" / "outputs" / "response.md",
        "quality.present-tense.body": repo_root / "skills" / "novel-coauthoring-openclaw-workspace" / "iteration-3" / "eval-2-present-tense-pacing" / "with_skill" / "outputs" / "response.md",
    }
    checks = {
        "contract.audit.rollback.chain": ["request_id", "session_id", "input_summary", "model_route", "persist_result", "rollback_from", "rollback_to"],
        "contract.asset.consistency": ["conflicts", "level", "fix", "affected_paths"],
        "integration.openclaw.retry.idempotent": ["X-Client-Id", "X-Timestamp", "X-Nonce", "X-Signature", "idempotent_replay=true", "latency_ms", "prompt_tokens", "completion_tokens"],
    }

    failures = []
    for case in matrix.get("cases", []):
        cid = case["id"]
        target = targets.get(cid)
        if not target or not target.exists():
            failures.append(f"{cid}: 目标文件不存在")
            continue
        text = target.read_text(encoding="utf-8")
        if cid in checks:
            miss = must_contain(text, checks[cid])
            if miss:
                failures.append(f"{cid}: 缺少字段 {', '.join(miss)}")
        if cid == "quality.present-tense.body":
            words = case["expect"]["body_rules"]["forbidden_words"]
            bad = [w for w in words if w in text]
            if bad:
                failures.append(f"{cid}: 命中禁用词 {', '.join(bad)}")
            if not has_paragraph(text):
                failures.append(f"{cid}: 未检测到自然段落")

    print(f"suite={matrix.get('suite')} version={matrix.get('version')} cases={len(matrix.get('cases', []))}")
    if failures:
        for f in failures:
            print(f"[FAIL] {f}")
        return 1
    print("[PASS] 所有评测断言通过")
    return 0


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[3]
    sys.exit(run(root))
