import requests
from solana.constants import LAMPORTS_PER_SOL
from retrying import retry


class ClusterClient:
    def __init__(self, endpoint="https://api.mainnet-beta.solana.com"):
        self.endpoint = endpoint

    @retry(stop_max_attempt_number=3)
    def get_balance(self, address_string='D27DgiipBR5dRdij2L6NQ27xwyiLK5Q2DsEM5ML5EuLK'):
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "jsonrpc": "2.0", "id": 1,
            "method": "getBalance",
            "params": [
                address_string
            ]
        }

        cluster_response = None

        try:
            cluster_response = requests.post(url=self.endpoint, headers=headers, json=payload)
        except Exception as e:
            print(f"请求异常, 异常信息: {e.args}")
            print(f'尝试次重新连接..')

        if cluster_response.status_code == 200:
            return {'value': cluster_response.json().get('result').get('value') / LAMPORTS_PER_SOL}
        else:
            print(f'状态码异常: {cluster_response.status_code}')

    @retry(stop_max_attempt_number=3)
    def get_token_accounts_by_owner(self, address_string='D27DgiipBR5dRdij2L6NQ27xwyiLK5Q2DsEM5ML5EuLK',
                                    hide_zero_token=True):
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getTokenAccountsByOwner",
            "params": [
                address_string,
                {
                    "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
                },
                {
                    "encoding": "jsonParsed"
                }
            ]
        }
        cluster_response = None
        owner_token_list = []
        try:
            cluster_response = requests.post(url=self.endpoint, headers=headers, json=payload)
        except Exception as e:
            print(f"请求异常, 异常信息: {e.args}")
            print(f'尝试次重新连接..')

        if cluster_response.status_code == 200:
            token_accounts_values = cluster_response.json().get('result').get("value")
            for token_account in token_accounts_values:
                item = {
                    'Account': token_account.get('pubkey'),
                    'Token': token_account.get('account').get('data').get('parsed').get('info').get('mint'),
                    'TokenBalance': token_account.get('account').get('data').get('parsed').get('info').get(
                        'tokenAmount').get('uiAmount'),

                }
                if hide_zero_token:
                    if item.get('TokenBalance'):
                        owner_token_list.append(item)
                else:
                    owner_token_list.append(item)
            return owner_token_list
        else:
            print(f'状态码异常: {cluster_response.status_code}')

    @retry(stop_max_attempt_number=3)
    def request_airdrop(self, address_string='D27DgiipBR5dRdij2L6NQ27xwyiLK5Q2DsEM5ML5EuLK', endpoint=None):
        if endpoint:
            endpoint = endpoint
        else:
            endpoint = self.endpoint

        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "jsonrpc": "2.0", "id": 1,
            "method": "requestAirdrop",
            "params": [
                address_string,
                int(1e9)
            ]
        }
        try:
            cluster_response = requests.post(url=endpoint, headers=headers, json=payload)
        except:
            raise

        if cluster_response.status_code == 200:
            print(cluster_response.json())
        else:
            print(cluster_response.json())



