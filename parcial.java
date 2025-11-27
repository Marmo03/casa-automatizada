import java.util.ArrayList;
import java.util.List;
import java.util.Random;

class Jugador {
    private String nombre;
    private int monedas;
    private List<String> inventario;

    public Jugador(String nombre) {
        this.nombre = nombre;
        this.monedas = 0;
        this.inventario = new ArrayList<>();
    }

    // Proteger acceso a monedas e inventario
    public synchronized void agregarMonedas(int cantidad) {
        monedas += cantidad;
    }

    public synchronized void agregarItem(String item) {
        inventario.add(item);
    }

    // Método opcional para mostrar el estado final de forma segura
    public synchronized String getEstado() {
        return "Jugador: " + nombre +
               "\nMonedas: " + monedas +
               "\nInventario: " + inventario;
    }
}

class Mision implements Runnable {

    private static final String[] ITEMS = {"Espada", "Poción", "Escudo"};
    private static final Random random = new Random();

    private Jugador jugador;
    private String nombreMision;

    public Mision(Jugador jugador, String nombreMision) {
        this.jugador = jugador;
        this.nombreMision = nombreMision;
    }

    @Override
    public void run() {
        // Simular recompensas de la misión
        int monedasGanadas = random.nextInt(100) + 1; // 1 a 100
        String itemGanado = ITEMS[random.nextInt(ITEMS.length)];

        // Actualizar al jugador (secciones críticas protegidas dentro de Jugador)
        jugador.agregarMonedas(monedasGanadas);
        jugador.agregarItem(itemGanado);

        // Mensaje para ver qué hizo cada hilo
        System.out.println("[" + nombreMision + "] " +
                "ganó " + monedasGanadas + " monedas y el ítem: " + itemGanado);
    }
}

public class JuegoRecompensas {
    public static void main(String[] args) {
        // Crear un jugador
        Jugador jugador = new Jugador("Juan");

        // Crear 3 misiones (3 hilos) que comparten el mismo jugador
        Thread mision1 = new Thread(new Mision(jugador, "Misión 1"));
        Thread mision2 = new Thread(new Mision(jugador, "Misión 2"));
        Thread mision3 = new Thread(new Mision(jugador, "Misión 3"));

        // Iniciar las misiones concurrentemente
        mision1.start();
        mision2.start();
        mision3.start();

        // Esperar a que todas terminen (join)
        try {
            mision1.join();
            mision2.join();
            mision3.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Mostrar estado final del jugador
        System.out.println("\n=== ESTADO FINAL DEL JUGADOR ===");
        System.out.println(jugador.getEstado());
    }
}