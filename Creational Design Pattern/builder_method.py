from abc import ABC,abstractmethod

class RemoteControl(ABC):
    @abstractmethod
    def switch_on(self):
        pass
    @abstractmethod
    def switch_off(self):
        pass


# Step 2 – Concrete Implementations (Devices)
class AC(RemoteControl):
    def switch_on(self):
        print('AC switched ON')

    def switch_off(self):
        print('AC switched OFF')


class TV(RemoteControl):
    def switch_on(self):
        print('TV switched ON')

    def switch_off(self):
        print('TV switched OFF')


class Fan(RemoteControl):
    def switch_on(self):
        print('Fan switched ON')

    def switch_off(self):
        print('Fan switched OFF')


class TapeRecorder(RemoteControl):
    def switch_on(self):
        print('Tape Recorder switched ON')

    def switch_off(self):
        print('Tape Recorder switched OFF')


class TvRemortecontrol:
    def __init__(self,tv:RemoteControl):
        self.tv=tv

    def turn_on(self):
        self.tv.switch_on()

    def turn_off(self):
        self.tv.switch_off()

    def volume_incress(self):
        print("volume incressed")

class Fanremotecontrol:
    def __init__(self,fan: RemoteControl):
        self.fan = fan

    def turn_on(self):
        self.fan.switch_on()

    def turn_off(self):
        self.fan.switch_off()

    def volume_incress(self):
        print("incress speed")


class AcRemotecontrol:
    def __init__(self,ac: RemoteControl):
        self.ac = ac

    def turn_on(self):
        self.ac.switch_on()

    def turn_off(self):
        self.ac.switch_off()

    def incress_temp(self):
        print("temp incressed")


class TapeRecordRemoteControl(TvRemortecontrol):

    def insert_casset(self):
        print("casset inserted")

    def play(self):
        print("casset play")


tv = TvRemortecontrol(TV())
tv.turn_on()
tv.turn_off()
tv.volume_incress()
print('-----------------------------')

radio = TapeRecordRemoteControl(TapeRecorder())
radio.turn_on()
radio.turn_off()
radio.volume_incress()
print("------------------------------")

ac =AcRemotecontrol(AC())
ac.turn_on()
ac.turn_off()
ac.incress_temp()
print("------------------------------")