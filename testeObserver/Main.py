from abc import ABC, abstractmethod

# Implementação da interface (com o @abstract method) do Observer. Isso permite que a interface seja chamada caso
# outras classes sejam utilizadas (o que não é o caso, nesse exemplo ela é opcional).
class InterfaceObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


# Classe concreta do Observer
class ConcreteObserver(InterfaceObserver):
    def __init__(self, name):
        self.name = name

    # método que efetivamente notifica o observer de alguma atualização
    def update(self, message):
        print(f"{self.name} recebeu a mensagem: {message}")


# Classe Subject -> classe que é observada
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


# Teste com exemplo de uso
if __name__ == "__main__":
    # Criando os observadores
    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")

    # Criando o subject
    subject = Subject()

    # Adicionando os observadores ao subject (que é uma lista)
    subject.add_observer(observer1)
    subject.add_observer(observer2)

    # Notificando observadores
    subject.notify_observers("Mensagem de teste")
