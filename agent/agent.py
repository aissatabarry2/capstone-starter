"""Squelette d'agent ops sans LLM : regles fixes, liste autorisee, approbation."""
import subprocess
import time

READ = ("kubectl get", "kubectl describe", "kubectl logs")
WRITE = ("kubectl rollout restart",)


def audit(cmd: str, approved: bool) -> None:
    with open("audit.log", "a") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} | {cmd} | approved={approved}\n")


def run_tool(cmd: str, approved: bool = False) -> str:
    if not (cmd.startswith(READ) or (cmd.startswith(WRITE) and approved)):
        raise PermissionError("refuse : liste autorisee ou approbation")
    audit(cmd, approved)
    return subprocess.run(cmd.split(), check=False, capture_output=True, text=True).stdout


if __name__ == "__main__":
    print(run_tool("kubectl get pods -n capstone"))
    ok = input("Redemarrer le deploiement ? (oui/non) ") == "oui"
    if ok:
        print(run_tool("kubectl rollout restart deploy/capstone-api -n capstone", approved=True))
