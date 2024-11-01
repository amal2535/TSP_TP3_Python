##unittest , pytest, logtest
import pytest


def test_respecter_capacite():
    TravelingSalesman = TravelingSalesman(capacite_max=10)
    assert TravelingSalesman.vehicle_capacity(10) == True
    assert TravelingSalesman.vehicle_capacity(11) == False