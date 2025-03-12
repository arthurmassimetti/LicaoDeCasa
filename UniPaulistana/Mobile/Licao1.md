# Correção dos Bugs - Aula 01 React Native

## Melhorias Implementadas:
1. **Mensagem randomizada sem perder efeitos visuais**
2. **Cores de fundo randomizadas a cada clique**
3. **Botão desaparecendo 2 segundos após o clique**

## Código Corrigido:

```jsx
import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Animated } from 'react-native';

const mensagens = [
  'Olá, mundo!',
  'React Native é incrível!',
  'Aprendendo e evoluindo!',
  'Persistência leva ao sucesso!',
  'Continue tentando!'
];

const getRandomMensagem = () => mensagens[Math.floor(Math.random() * mensagens.length)];
const getRandomColor = () => `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})`;

const App = () => {
  const [mensagem, setMensagem] = useState(getRandomMensagem());
  const [corFundo, setCorFundo] = useState(getRandomColor());
  const [mostrarBotao, setMostrarBotao] = useState(true);
  
  const handlePress = () => {
    setMensagem(getRandomMensagem());
    setCorFundo(getRandomColor());
    setMostrarBotao(true);
    
    setTimeout(() => {
      setMostrarBotao(false);
    }, 2000);
  };

  return (
    <View style={[styles.container, { backgroundColor: corFundo }]}> 
      <Text style={styles.texto}>{mensagem}</Text>
      {mostrarBotao && (
        <TouchableOpacity style={styles.botao} onPress={handlePress}>
          <Text style={styles.botaoTexto}>Clique Aqui</Text>
        </TouchableOpacity>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  texto: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 20,
  },
  botao: {
    backgroundColor: '#000',
    padding: 10,
    borderRadius: 5,
  },
  botaoTexto: {
    color: '#fff',
    fontSize: 16,
  },
});

export default App;
```

## O que foi corrigido?
- **Linha Eliminada:** Removida a reinicialização incorreta da animação visual.
- **Mensagens agora são randomizadas corretamente.**
- **Cores de fundo mudam a cada clique.**
- **Botão desaparece após 2 segundos ao ser clicado.**

## Como testar?
1. Instale o React Native no seu ambiente.
2. Copie o código acima para um arquivo `App.js`.
3. Execute o app no seu celular ou emulador com `npx react-native run-android` ou `npx expo start`.
4. Teste clicando no botão e observe as mudanças.
