import unittest

from PyViCare.PyViCareHeatPump import HeatPump
from tests.ViCareServiceMock import ViCareServiceMock


class Vitocal200S(unittest.TestCase):
    def setUp(self):
        self.service = ViCareServiceMock('response/Vitocal200S.json')
        self.device = HeatPump(self.service)

    def test_getDomesticHotWaterConfiguredTemperature(self):
        self.assertEqual(
            self.device.getDomesticHotWaterConfiguredTemperature(), 40)

    def test_getAvailableCompressors(self):
        self.assertEqual(self.device.getAvailableCompressors(), ['0'])

    def test_getDomesticHotWaterConfiguredTemperature2(self):
        self.assertEqual(
            self.device.getDomesticHotWaterConfiguredTemperature2(), 60)

    def test_getReturnTemperature(self):
        self.assertEqual(
            self.device.getReturnTemperature(), 27.9)

    def test_getSupplyTemperaturePrimaryCircuit(self):
        self.assertEqual(
            self.device.getSupplyTemperaturePrimaryCircuit(), 14.5)

    def test_getReturnTemperatureSecondaryCircuit(self):
        self.assertEqual(
            self.device.getReturnTemperatureSecondaryCircuit(), 27.9)

class Vitocal200S_Paid(unittest.TestCase):
    def setUp(self):
        self.service = ViCareServiceMock('response/Vitocal200S-paid.json')
        self.device = HeatPump(self.service)

    def test_getBoilerTemperatureCommonSupply(self):
        self.assertEqual(
            self.device.getBoilerTemperatureCommonSupply(), 48)

    def test_getTemperature(self):
        self.assertEqual(
            self.device.circuits[0].getTemperature(), 37.3)
        self.assertEqual(
            self.device.circuits[1].getTemperature(), 46.8)

    def test_getProductionCoolingWeek(self):
        self.assertEqual(
            self.device.compressors[0].getProductionCoolingWeek(), 0)
        self.assertEqual(
            self.device.compressors[0].getProductionCoolingWeekUnit(), "kilowattHour")

    def test_getProductionCurrent(self):
        self.assertEqual(
            self.device.compressors[0].getProductionCurrent(), 6817)
        self.assertEqual(
            self.device.compressors[0].getProductionCurrentUnit(), "watt")

    def test_getProductionDomesticHotWaterWeek(self):
        self.assertEqual(
            self.device.compressors[0].getProductionDomesticHotWaterWeek(), 0)
        self.assertEqual(
            self.device.compressors[0].getProductionDomesticHotWaterWeekUnit(), "kilowattHour")

    def test_getProductionHeatingWeek(self):
        self.assertEqual(
            self.device.compressors[0].getProductionHeatingWeek(), 311.7)
        self.assertEqual(
            self.device.compressors[0].getProductionHeatingWeekUnit(), "kilowattHour")

    def test_getConsumptionCoolingWeek(self):
        self.assertEqual(
            self.device.compressors[0].getConsumptionCoolingWeek(), 0)
        self.assertEqual(
            self.device.compressors[0].getConsumptionCoolingWeekUnit(), "kilowattHour")

    def test_getConsumptionCurrent(self):
        self.assertEqual(
            self.device.compressors[0].getConsumptionCurrent(), 2327)
        self.assertEqual(
            self.device.compressors[0].getConsumptionCurrentUnit(), "watt")

    def test_getConsumptionDomesticHotWaterWeek(self):
        self.assertEqual(
            self.device.compressors[0].getConsumptionDomesticHotWaterWeek(), 0)
        self.assertEqual(
            self.device.compressors[0].getConsumptionDomesticHotWaterWeekUnit(), "kilowattHour")

    def test_getConsumptionHeatingWeek(self):
        self.assertEqual(
            self.device.compressors[0].getConsumptionHeatingWeek(), 105.7)
        self.assertEqual(
            self.device.compressors[0].getConsumptionHeatingWeekUnit(), "kilowattHour")
