class AlpacaCryptoApiError(Exception):
    """Custom exception for errors related to Alpaca Crypto API."""
    
    def __init__(self, message="Error fetching Alpaca crypto data"):
        self.message = message
        super().__init__(self.message)