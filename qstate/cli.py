import argparse,json
from .features import execute,sample,expectation_z
def main():
    parser=argparse.ArgumentParser(description='Simulate a small circuit described by JSON')
    parser.add_argument('circuit');parser.add_argument('--shots',type=int,default=1000);parser.add_argument('--seed',type=int,default=0)
    args=parser.parse_args()
    try:
        with open(args.circuit) as f:config=json.load(f)
        state=execute(config['qubits'],config['operations'])
        print(json.dumps({'counts':sample(state,args.shots,args.seed),'z0':expectation_z(state,0)},sort_keys=True))
    except (ValueError,KeyError,OSError,TypeError) as error:parser.error(str(error))
