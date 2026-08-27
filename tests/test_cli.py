import subprocess,sys
def test_help():
    result=subprocess.run([sys.executable,'-m','qstate','--help'],text=True,capture_output=True)
    assert result.returncode==0 and 'usage:' in result.stdout
def test_cli_rejects_unknown_argument():
    result=subprocess.run([sys.executable,'-m','qstate','--unknown-option'],text=True,capture_output=True)
    assert result.returncode!=0

def test_documented_workflow():
    import json
    result=subprocess.run([sys.executable,'-m','qstate',*['examples/bell.json','--shots','200','--seed','7']],text=True,capture_output=True)
    assert result.returncode==0, result.stderr
    data=json.loads(result.stdout)
    assert sum(data['counts'].values())==200 and set(data['counts'])=={'00','11'}
