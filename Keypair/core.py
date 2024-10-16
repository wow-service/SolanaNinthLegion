from solana.rpc.api import Keypair
import bip39
from mnemonic import Mnemonic


def new(strength=128):
    mnem = Mnemonic(language='english')
    words = mnem.generate(strength=strength)
    seed = bip39.phrase_to_seed(words)
    owner = Keypair.from_seed(seed[:32])
    data = {
        'MNEMONIC': words,
        'ADDRESS': owner.pubkey().__str__(),
        'HEX': ''.join([hex(item)[2:].zfill(2) for item in owner.to_bytes_array()[:32]]),
        'BS58': owner.__str__(),
        'UINT8': owner.to_bytes_array(),
    }
    return data

