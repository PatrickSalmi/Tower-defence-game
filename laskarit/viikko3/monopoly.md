```mermaid
---
title: Monopoli
---
classDiagram
    Pelaajat "1" <-- Pelinappula
    Pelinappula "1" -- "1..8" Ruudut
    Pelinappula "2..8" -- "1" Pelilauta
    Ruudut "40" -- "1" Pelilauta
    Pelaajat "1" ..|> "2" Nopat

    class Nopat{
    }
    class Pelaajat{
    }
    class Pelinappula{
    }
    class Pelilauta{
    }
    class Ruudut{
    }

```
