Register: __log__({ign: bytes32, addr: address})
Update: __log__({ign: bytes32, oldAddr: address, newAddr: address})

owner: address

# -------------------------------------------
# ---------- State Variables ----------------
# -------------------------------------------

# Represents the IGN associated to an address
names: public(bytes32[address])
# Represents the address associated to an IGN
addresses: public(address[bytes32])


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
    assert self.names[msg.sender] == as_bytes32(0)
    self.names[msg.sender] = ign
    self.addresses[ign] = msg.sender
    log.Register(ign, msg.sender)

@public
def changeAddress (newAddress: address):
    # Expect sender to have an IGN registered
    assert self.names[msg.sender] != as_bytes32(0)
    
    # Expect new address not to be registered already
    assert self.names[newAddress] == as_bytes32(0)
    
    # Get current IGN
    ign = self.names[msg.sender]
    
    # Change address associated to IGN
    self.addresses[ign] = newAddress
    
    # Change name associated to address
    self.names[newAddress] = ign
    
    # Remove old address registration
    self.names[msg.sender] = None
    
    log.Update(ign, msg.sender, newAddress)
