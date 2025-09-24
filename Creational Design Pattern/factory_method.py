from abc import ABC,abstractmethod
class Notificationfactory(ABC):
    @abstractmethod
    def create_notification(self):
        pass

class Emailnotificationfactory(Notificationfactory):
    def create_notification(self):
        return Emailnotification()



class Phonenotificationfactory(Notificationfactory):
    def create_notification(self):
        return Phonenotification()


class Smsnotificationfactory(Notificationfactory):
    def create_notification(self):
        return Smsnotification()



class Notificationinterface(ABC):
    @abstractmethod
    def notify(self,message):
        pass


class Emailnotification(Notificationinterface):
    def notify(self,message):
        print(f" send emailmsg {message}")


class Phonenotification(Notificationinterface):
    def notify(self,message):
        print(f" send phonemsg {message}")


class Smsnotification(Notificationinterface):
    def notify(self,message):
        print(f" send smsmsg {message}")


def send_notification(notification_factory:Notificationfactory,message):
    if isinstance(notification_factory,Notificationfactory):
        notifir:Notificationinterface=notification_factory.create_notification()
        notifir.notify(message)

email_notif=Emailnotificationfactory()
send_notification(email_notif,"hello")

phone_notif=Phonenotificationfactory()
send_notification(phone_notif,"hello")

sms_notif=Smsnotificationfactory()
send_notification(sms_notif,"hello")
