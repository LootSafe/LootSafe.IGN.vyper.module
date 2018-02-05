owner: address

# -------------------------------------------
# ---------- State Variables ----------------
# -------------------------------------------

# Represents the IGN associated to an address
names: bytes32[address]
# Represents the address associated to an IGN
addresses: address[bytes32]

# -------------------------------------------
# -------------- Internal -------------------
# -------------------------------------------

@public
def __init__ ():
    self.owner = msg.sender
    
# -------------------------------------------
# -------------- Getters --------------------
# -------------------------------------------

@public
def getAddress (ign: bytes32) -> address:
    # Return the address of an IGN
    return self.addresses[ign]


# -------------------------------------------
# -------------- External -------------------
# -------------------------------------------

@public
def register (ign: bytes32):
    # If address is not already registered to an IGN register it
    assert not self.names[msg.sender]
    self.names[msg.sender] = ign
    self.addresses[ign] = msg.sender

@public
def changeAddress (newAddress: address):
    # Expect sender to have an IGN registered
    assert self.names[msg.sender]
    
    # Expect new address not to be registered already
    assert not self.names[newAddress]
    
    # Get current IGN
    ign = self.names[msg.sender]
    
    # Change address associated to IGN
    self.addresses[ign] = newAddress
    
    # Change name associated to address
    self.names[newAddress] = ign
    
    # Remove old address registration
    self.names[msg.sender] = null
