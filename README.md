# LootSafe.IGN.vyper.module

# Overview
The IGN module is used to associate a human friendly name to an Ethereum address. This can be used to prevent MITM attacks to some extent as well as create a pleasant friendslist for blockchain backed games.

For example Matt#ae34f will return Matt's address.


# Documentation
## Methods

### getAddress

Returns the address associated to an IGN

```py
def getAddress (ign: bytes <= 32) -> address:
```

### register

Register a new IGN associated with your address. Usernames should be no more than 26 bytes.

```py
def register (ign: bytes <= 26):
```

**Event:** `Register: __log__({ign: bytes <= 32, addr: address})`

### changeAddress

Change the address associated to `msg.sender`s IGN.

```py
def changeAddress (newAddress: address):
```

**Event:** `Update: __log__({ign: bytes <= 32, oldAddr: address, newAddr: address})`

