public class Singleton {

    // O static torna a variável instance (a própria instância da classe Singleton estática, podendo ser acessada
    // diretamente sem necessitar de )
    private static Singleton instancia;

    // construtor privado
    private Singleton() {
    }

    // esse método retorna a instância de singleton caso já exista uma, ou cria uma caso contrário
    public static Singleton getInstancia() {
        if (instancia == null) {
            instancia = new Singleton();
        }
        return instancia;
    }

    public static void main(String[] args) {
        Singleton singleton = Singleton.getInstancia ();
        Singleton singleton1 = Singleton.getInstancia ();

        // o sysout mostra duas instancias que se referem a um mesmo objeto armazenado no mesmo local da memória
        System.out.println(singleton);
        System.out.println(singleton1);
    }
}
