"""hello_world main module."""

import sys
import hvac


def main():
    # authenticate to Vault
    client = hvac.Client(
        url='http://127.0.0.1:8200',
        token='dev-only-token',
    )

    # store a secret
    create_response = client.secrets.kv.v2.create_or_update_secret(
        path='my-secret-password',
        secret={"password": 'Hashi123'}
    )

    print('Secret written successfully.')

    # retrieve a secret
    read_response = client.secrets.kv.read_secret_version(path='my-secret-password')
    password = read_response['data']['data']['password']
    if password != 'Hashi123':
        sys.exit('unexpected password')

    print('Access granted!')

if __name__ == '__main__':
    main()
