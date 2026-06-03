# Bebedouro Inteligente para Pets

## Integrantes do Grupo:
- Diego Mourão Oliveira
- Ilan Hameiry
- Luca Lopes Martinho

## Descrição do Projeto

O projeto consiste no desenvolvimento de um dispositivo IoT voltado para o fornecimento de água corrente para animais de estimação (pets), com foco em uso residencial.

O objetivo principal é oferecer uma forma mais atrente e confortável de hidratação para o animal, simulando o fluxo de água corrente, além de monitorar a frequência com que o pet utiliza o bebedouro.

O sistema será ativado automaticamente apenas quando houver presença do animal próxima ao dispositivo, evitando desperdício de energia e água.

## Funcionamento do Sistema

O bebedouro funcionará em ciclo contínuo de circulação de água entre a bomba e o reservatório, simulando água corrente.

Por meio de um sensor de presença por distância (ultrassônico), o sistema será ativado automaticamente quando o animal se aproximar.

Após a detecção, o dispositivo permanecerá ligado por alguns segundos mesmo após a ausência de presença, garantindo tempo suficiente para o pet se hidratar.

Além disso, o sistema contará com:

- Iluminação interna por LEDs, acionada automaticamente quando a luminosidade do ambiente estiver baixa;
- Display informativo com dados importantes de uso;
- Monitoramento do nível de água no reservatório;
- Alertas de nível baixo de água;
- Botão de ativação manual;
- Botão de reset do sistema;
- Envio de notificações e informações para um software externo via Bluetooth.

## Objetivos do Projeto

- Melhorar a experiência de hidrtação dos pets;
- Automatizar o fornecimento de água;
- Reduzir desperdícios de energia e água;
- Permitir o monitoramento do uso do bebedouro;
- Fornecer alertas e informações em tempo real ao usuário.

## Requisitos do Sistema

### Requisitos Obrigatórios

| ID | Requisito | Tipo |
|---|---|---|
| RO-01 | Água circulando entre bomba e funil | Obrigatório |
| RO-02 | Detector de presença por distância (sensor ultrassônico) | Obrigatório |
| RO-03 | Iluminação em LED quando necessário | Obrigatório |
| RO-04 | Botão para ativação manual | Obrigatório |
| RO-05 | Botão de reset | Obrigatório |

### Requisitos Desejáveis

| ID | Requisito | Tipo |
|---|---|---|
| RD-01 | Display com informações úteis de uso: nível de água e número de ativações | Desejável |
| RD-02 | Mensagem via Bluetooth quando houver presença detectada ou nível baixo de água | Desejável |
| RD-03 | Sensor de nível de água | Desejável |

### Requisitos Opcionais

| ID | Requisito | Tipo |
|---|---|---|
| ROP-03 | Programação de ativação em intervalos de tempo definidos | Opcional |

## Diagrama de Blocos
```mermaid
flowchart TD
    MCU["Microcontrolador<br/>(Raspberry Pi Pico)"]

    OLED["Display<br/>OLED I2C<br/>128x32 Px"]
    RTC["Módulo Real Time Clock<br/>DS1307 (Opcional)"]
    LDR["Sensor de Luz<br/>LDR"]
    SOIL["Sensor de nível<br/>de água"]
    BT["Módulo Bluetooth<br/>HM10"]

    LEVEL1["Conversor de Nível Lógico<br/>(5V ↔ 3.3V)"]
    US["Sensor de Distância<br/>Ultrassom HC-SR04"]

    LEVEL2["Conversor de Nível Lógico<br/>(5V ↔ 3.3V)"]
    RELAY["Módulo Relé"]
    PUMP["Mini Bomba de Água<br/>DC-JT160"]

    MCU --> OLED 
    RTC --> MCU
    LDR --> MCU
    SOIL --> MCU
    MCU --> BT

    US --> LEVEL1
    LEVEL1 --> MCU

    MCU --> LEVEL2
    LEVEL2 --> RELAY
    RELAY --> PUMP

    %% Optional styling
    classDef sensor fill:#cfe8f3,stroke:#333,stroke-width:1px;
    classDef converter fill:#f4c542,stroke:#333,stroke-width:1px;
    classDef relay fill:#6abf4b,stroke:#333,stroke-width:1px;
    classDef controller fill:#cfe8f3,stroke:#333,stroke-width:2px;

    class MCU controller;
    class OLED,RTC,LDR,SOIL,BT,US,PUMP sensor;
    class LEVEL1,LEVEL2 converter;
    class RELAY relay;
    classDef default fill:#cfe8f3,color:#000,stroke:#000,stroke-width:2px;

    linkStyle default stroke:#000,stroke-width:2px;
```

## Softwares Utilizados

Durante o desenvolvimento do projeto foram utilizados os seguintes softwares:

- KiCad — utilizado para esquematização eletrônica e desenvolvimento do diagrama/layout da PCB;
- Thonny — utilizado para programação, testes e depuração do Raspberry Pi Pico;
- Autodesk Fusion 360, Solidworks — utilizados para modelagem 3D da estrutura do bebedouro;

## Tecnologias Envolvidas

O projeto utiliza conceitos de:

- Internet das Coisas (IoT)
- Sensores ultrassônicos
- Sensores de nível de água
- Iluminação automatizada com LEDs
- Comunicação via Bluetooth
- Sistemas embarcados
- Automação residencial

## Imagens do Modelo

![Vista Frontal](./media/images/bebedouro_vista_frontal.png) ![Vista Lateral](./media/images/bebedouro_vista_lateral.png)
![Vista Superior](./media/images/bebedouro_vista_superior.png) ![Vista Tridimensional](./media/images/bebedouro_vista_tridimensional.png)

