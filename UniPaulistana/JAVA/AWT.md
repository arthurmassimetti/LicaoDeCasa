```java
import java.awt.*;

public class Awtl {
    public static void main(String[] args) {
        Frame frame = new Frame("Exemplo AWT");
        Label label = new Label("Olá, mundo!");

        frame.add(label);
        frame.setSize(300, 200);
        frame.setVisible(true);
    }
}
```
```java
import java.awt.*;
public class Awt2 {
    public static void main(String[] args) {
        Frame frame = new Frame("Exemplo de Layout");

        Panel panel = new Panel();
        panel.setLayout(new FlowLayout());

        panel.add(new Button("Botão 1"));
        panel.add(new Button("Botão 2"));
        panel.add(new Button("Botão 3"));

        frame.add(panel);
        frame.setSize(300, 200);
        frame.setVisible(true);
    }
}

```

```java
import java.awt.*;

public class Awt3 extends Canvas {
    public static void main(String[] args) {
        Frame frame = new Frame("Exemplo de Desenho AWT");
        Canvas canvas = new Awt3();

        frame.add(canvas);
        frame.setSize(400, 300);
        frame.setVisible(true);
    }

    @Override
    public void paint(Graphics g) {
        g.setColor(Color.RED);
        g.drawLine(50, 50, 150, 150);

        g.setColor(Color.BLUE);
        g.fillRect(200, 50, 100, 100);

        g.setColor(Color.GREEN);
        g.fillOval(100, 200, 150, 150);
    }
}

```

```java
import java.awt.*;

public class Awt4 {
    public static void main(String[] args) {
        Frame frame = new Frame("Exemplo de Componentes de Texto AWT");
        TextField textField = new TextField("Digite aqui");
        TextArea textArea = new TextArea("Área de texto", 5, 30);

        frame.setLayout(new FlowLayout());
        frame.add(textField);
        frame.add(textArea);
        
        frame.setSize(300, 200);
        frame.setVisible(true);
    }
}

```
