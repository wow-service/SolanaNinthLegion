import json

from Keypair.core import new
from Tools.core import ClusterClient

if __name__ == '__main__':
    # account = new()
    # pretty_account = json.dumps(account, indent=4)
    # print(pretty_account)

    address = 'D27DgiipBR5dRdij2L6NQ27xwyiLK5Q2DsEM5ML5EuLK'
    endpoint = 'https://mainnet.helius-rpc.com/?api-key=be2d273e-e71f-4cd7-b7a7-81fed6d0a7c0'
    cluster_cli = ClusterClient(endpoint)
    values = cluster_cli.get_balance(address_string=address)

    token_accounts = cluster_cli.get_token_accounts_by_owner(address_string=address)

    pretty_value = json.dumps(values, indent=4)
    print(pretty_value)

    pretty_token_accounts = json.dumps(token_accounts, indent=4)
    print(pretty_token_accounts)
