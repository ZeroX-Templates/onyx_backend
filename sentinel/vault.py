# vault.py
class Vault:
    def __init__(self):
        self.secrets = {}

    def add_secret(self, label, secret):
        self.secrets[label] = secret

    def list_secrets(self):
        return list(self.secrets.keys())

    def get_secret(self, label):
        return self.secrets.get(label)
