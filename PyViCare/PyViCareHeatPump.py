from typing import Any, List

from PyViCare.PyViCareHeatingDevice import (HeatingDevice,
                                            HeatingDeviceWithComponent)
from PyViCare.PyViCareUtils import handleNotSupported


class HeatPump(HeatingDevice):

    @property
    def compressors(self) -> List[Any]:
        return list([self.getCompressor(x) for x in self.getAvailableCompressors()])

    def getCompressor(self, compressor):
        return Compressor(self, compressor)

    @handleNotSupported
    def getAvailableCompressors(self):
        return self.service.getProperty("heating.compressors")["properties"]["enabled"]["value"]

    @handleNotSupported
    def getBufferMainTemperature(self):
        return self.service.getProperty("heating.buffer.sensors.temperature.main")["properties"]['value']['value']

    @handleNotSupported
    def getBufferTopTemperature(self):
        return self.service.getProperty("heating.buffer.sensors.temperature.top")["properties"]['value']['value']

    # Power consumption for Heating:
    @handleNotSupported
    def getPowerSummaryConsumptionHeatingUnit(self):
        return self.service.getProperty("heating.power.consumption.summary.heating")["properties"]["currentDay"]["unit"]

    @handleNotSupported
    def getPowerSummaryConsumptionHeatingCurrentDay(self):
        return self.service.getProperty("heating.power.consumption.summary.heating")["properties"]["currentDay"]["value"]

    @handleNotSupported
    def getPowerSummaryConsumptionHeatingCurrentMonth(self):
        return self.service.getProperty("heating.power.consumption.summary.heating")["properties"]["currentMonth"]["value"]

    @handleNotSupported
    def getPowerSummaryConsumptionHeatingCurrentYear(self):
        return self.service.getProperty("heating.power.consumption.summary.heating")["properties"]["currentYear"]["value"]

    @handleNotSupported
    def getPowerSummaryConsumptionHeatingLastMonth(self):
        return self.service.getProperty("heating.power.consumption.summary.heating")["properties"]["lastMonth"]["value"]

    @handleNotSupported
    def getPowerSummaryConsumptionHeatingLastSevenDays(self):
        return self.service.getProperty("heating.power.consumption.summary.heating")["properties"]["lastSevenDays"]["value"]

    @handleNotSupported
    def getPowerSummaryConsumptionHeatingLastYear(self):
        return self.service.getProperty("heating.power.consumption.summary.heating")["properties"]["lastYear"]["value"]

    @handleNotSupported
    def getPowerConsumptionUnit(self):
        return self.service.getProperty("heating.power.consumption.total")["properties"]["day"]["unit"]

    @handleNotSupported
    def getPowerConsumptionToday(self):
        return self.service.getProperty("heating.power.consumption.total")["properties"]["day"]["value"][0]

    @handleNotSupported
    def getPowerConsumptionDomesticHotWaterToday(self):
        return self.service.getProperty("heating.power.consumption.dhw")["properties"]["day"]["value"][0]

    # Power consumption for Domestic Hot Water:
    @handleNotSupported
    def getPowerSummaryConsumptionDomesticHotWaterUnit(self):
        return self.service.getProperty("heating.power.consumption.summary.dhw")["properties"]["currentDay"]["unit"]

    @handleNotSupported
    def getPowerSummaryConsumptionDomesticHotWaterCurrentDay(self):
        return self.service.getProperty("heating.power.consumption.summary.dhw")["properties"]["currentDay"]["value"]

    @handleNotSupported
    def getPowerSummaryConsumptionDomesticHotWaterCurrentMonth(self):
        return self.service.getProperty("heating.power.consumption.summary.dhw")["properties"]["currentMonth"]["value"]

    @handleNotSupported
    def getPowerSummaryConsumptionDomesticHotWaterCurrentYear(self):
        return self.service.getProperty("heating.power.consumption.summary.dhw")["properties"]["currentYear"]["value"]

    @handleNotSupported
    def getPowerSummaryConsumptionDomesticHotWaterLastMonth(self):
        return self.service.getProperty("heating.power.consumption.summary.dhw")["properties"]["lastMonth"]["value"]

    @handleNotSupported
    def getPowerSummaryConsumptionDomesticHotWaterLastSevenDays(self):
        return self.service.getProperty("heating.power.consumption.summary.dhw")["properties"]["lastSevenDays"]["value"]

    @handleNotSupported
    def getPowerSummaryConsumptionDomesticHotWaterLastYear(self):
        return self.service.getProperty("heating.power.consumption.summary.dhw")["properties"]["lastYear"]["value"]

    @handleNotSupported
    def getBoilerTemperatureCommonSupply(self):
        return self.service.getProperty("heating.boiler.sensors.temperature.commonSupply")["properties"]["value"]["value"]

    @handleNotSupported
    def getVolumetricFlowReturn(self):
        return self.service.getProperty("heating.sensors.volumetricFlow.allengra")["properties"]['value']['value']


class Compressor(HeatingDeviceWithComponent):

    @property
    def compressor(self) -> str:
        return self.component

    @handleNotSupported
    def getStarts(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.statistics")["properties"]["starts"]["value"]

    @handleNotSupported
    def getHours(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.statistics")["properties"]["hours"]["value"]

    @handleNotSupported
    def getHoursLoadClass1(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.statistics")["properties"]["hoursLoadClassOne"]["value"]

    @handleNotSupported
    def getHoursLoadClass2(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.statistics")["properties"]["hoursLoadClassTwo"]["value"]

    @handleNotSupported
    def getHoursLoadClass3(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.statistics")["properties"]["hoursLoadClassThree"]["value"]

    @handleNotSupported
    def getHoursLoadClass4(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.statistics")["properties"]["hoursLoadClassFour"]["value"]

    @handleNotSupported
    def getHoursLoadClass5(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.statistics")["properties"]["hoursLoadClassFive"]["value"]

    @handleNotSupported
    def getActive(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}")["properties"]["active"]["value"]
    
    @handleNotSupported
    def getPhase(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}")["properties"]["phase"]["value"]

    @handleNotSupported
    def getProductionCoolingWeek(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.heat.production.cooling.week")["properties"]["value"]["value"]

    @handleNotSupported
    def getProductionCoolingWeekUnit(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.heat.production.cooling.week")["properties"]["value"]["unit"]

    @handleNotSupported
    def getProductionCurrent(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.heat.production.current")["properties"]["value"]["value"]

    @handleNotSupported
    def getProductionCurrentUnit(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.heat.production.current")["properties"]["value"]["unit"]

    @handleNotSupported
    def getProductionDomesticHotWaterWeek(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.heat.production.dhw.week")["properties"]["value"]["value"]

    @handleNotSupported
    def getProductionDomesticHotWaterWeekUnit(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.heat.production.dhw.week")["properties"]["value"]["unit"]

    @handleNotSupported
    def getProductionHeatingWeek(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.heat.production.heating.week")["properties"]["value"]["value"]

    @handleNotSupported
    def getProductionHeatingWeekUnit(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.heat.production.heating.week")["properties"]["value"]["unit"]

    @handleNotSupported
    def getConsumptionCoolingWeek(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.power.consumption.cooling.week")["properties"]["value"]["value"]

    @handleNotSupported
    def getConsumptionCoolingWeekUnit(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.power.consumption.cooling.week")["properties"]["value"]["unit"]

    @handleNotSupported
    def getConsumptionCurrent(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.power.consumption.current")["properties"]["value"]["value"]

    @handleNotSupported
    def getConsumptionCurrentUnit(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.power.consumption.current")["properties"]["value"]["unit"]

    @handleNotSupported
    def getConsumptionDomesticHotWaterWeek(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.power.consumption.dhw.week")["properties"]["value"]["value"]

    @handleNotSupported
    def getConsumptionDomesticHotWaterWeekUnit(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.power.consumption.dhw.week")["properties"]["value"]["unit"]

    @handleNotSupported
    def getConsumptionHeatingWeek(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.power.consumption.heating.week")["properties"]["value"]["value"]

    @handleNotSupported
    def getConsumptionHeatingWeekUnit(self):
        return self.service.getProperty(f"heating.compressors.{self.compressor}.power.consumption.heating.week")["properties"]["value"]["unit"]
