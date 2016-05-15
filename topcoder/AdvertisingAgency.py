class AdvertisingAgency:
    def numberOfRejections(self, requests):
        return len(requests) - len(set(requests))


agency = AdvertisingAgency()
assert agency.numberOfRejections((1, 2, 3)) == 0
assert agency.numberOfRejections((1, 2, 1, 2)) == 2
