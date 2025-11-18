# 🔐 Générateur de Mot de Passe Sécurisé

Un générateur de mot de passe moderne, sécurisé et sans dépendances externes écrit en Python pur.

## ✨ Caractéristiques

- ✅ **100% Python standard** - Aucune dépendance à installer
- 🔒 **Cryptographiquement sécurisé** - Utilise le module `secrets`
- 🎨 **Interface interactive** - Facile à utiliser pour tous
- 🛡️ **Configurable** - Personnalisez chaque aspect
- 📏 **Longueurs flexibles** - De 12 à 128+ caractères
- 🎯 **Options avancées** - Exclusion des caractères ambigus
- 📚 **Code moderne** - Type hints, dataclasses, docstrings

## 🚀 Utilisation

### Mode interactif (recommandé)

```bash
python main.py
```

Cela lance une interface interactive où vous pouvez :
- Définir la longueur du mot de passe
- Choisir les types de caractères à inclure
- Exclure les caractères ambigus si souhaité

### Mode script

```bash
python password_generator.py
```

Génère un mot de passe avec la configuration par défaut (16 caractères).

### Utilisation en tant que module

```python
from password_generator import PasswordGenerator, PasswordConfig

# Configuration personnalisée
config = PasswordConfig(
    length=20,
    include_uppercase=True,
    include_lowercase=True,
    include_digits=True,
    include_special=True,
    exclude_ambiguous=True
)

# Générer
generator = PasswordGenerator(config)
password = generator.generate()
print(password)
```

## 🔧 Configuration

### Paramètres disponibles

| Paramètre | Type | Défaut | Description |
|-----------|------|--------|-------------|
| `length` | int | 16 | Longueur du mot de passe (min: 12) |
| `include_uppercase` | bool | True | Inclure les majuscules (A-Z) |
| `include_lowercase` | bool | True | Inclure les minuscules (a-z) |
| `include_digits` | bool | True | Inclure les chiffres (0-9) |
| `include_special` | bool | True | Inclure les caractères spéciaux |
| `exclude_ambiguous` | bool | False | Exclure i, l, 1, O, 0 |

## 🔒 Sécurité

- Utilise `secrets.choice()` pour un tirage cryptographiquement sûr
- Garantit au moins un caractère de chaque catégorie sélectionnée
- Mélange sécurisé avec `secrets.randbelow()`
- Aucune dépendance externe (moins de risques de vulnérabilité)

## 💻 Prérequis

- Python 3.9+
- Aucune dépendance externe

## 📄 Licence

MIT

## 🤝 Contribution

Les contributions sont les bienvenues !
