## Diagrama - Base de Dados

```mermaid
flowchart
	. --> app --> db --> crud
                  db --> model
                  db --> repository
                  db --> schema
          app --> views --> v1
          app --> routes --> auth
                  routes --> credit_card
                  routes --> health
	. --> tests
    . --> docs
```
