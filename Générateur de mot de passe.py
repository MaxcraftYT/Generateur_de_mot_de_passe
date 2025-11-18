#!/usr/bin/env python3
"""
Générateur de mot de passe sécurisé
Module pour générer des mots de passe forts et sécurisés sans dépendances externes.
"""

import secrets
import string
from dataclasses import dataclass
from typing import Optional


@dataclass
class PasswordConfig:
    """Configuration pour la génération de mot de passe."""
    
    length: int = 16
    include_uppercase: bool = True
    include_lowercase: bool = True
    include_digits: bool = True
    include_special: bool = True
    exclude_ambiguous: bool = False
    
    def __post_init__(self) -> None:
        """Valider la configuration."""
        if self.length < 12:
            raise ValueError(
                "❌ La longueur doit être au minimum 12 caractères "
                "pour une sécurité adéquate."
            )
        
        if not any([
            self.include_uppercase,
            self.include_lowercase,
            self.include_digits,
            self.include_special
        ]):
            raise ValueError(
                "❌ Vous devez inclure au moins une catégorie de caractères."
            )


class PasswordGenerator:
    """Générateur de mot de passe sécurisé."""
    
    # Caractères spéciaux sûrs (excluant les plus ambigus)
    SPECIAL_CHARS = "!#$%&*+-=?@^_~"
    SPECIAL_CHARS_FULL = string.punctuation
    
    # Caractères ambigus souvent exclus
    AMBIGUOUS_CHARS = set("il1Lo0O")
    
    def __init__(self, config: Optional[PasswordConfig] = None) -> None:
        """
        Initialiser le générateur.
        
        Args:
            config: Configuration personnalisée ou None pour la configuration par défaut
        """
        self.config = config or PasswordConfig()
    
    def _build_character_pool(self) -> str:
        """
        Construire le pool de caractères disponibles.
        
        Returns:
            Chaîne contenant tous les caractères possibles
        """
        pool = ""
        
        if self.config.include_lowercase:
            chars = string.ascii_lowercase
            if self.config.exclude_ambiguous:
                chars = "".join(c for c in chars if c not in self.AMBIGUOUS_CHARS)
            pool += chars
        
        if self.config.include_uppercase:
            chars = string.ascii_uppercase
            if self.config.exclude_ambiguous:
                chars = "".join(c for c in chars if c not in self.AMBIGUOUS_CHARS)
            pool += chars
        
        if self.config.include_digits:
            chars = string.digits
            if self.config.exclude_ambiguous:
                chars = "".join(c for c in chars if c not in self.AMBIGUOUS_CHARS)
            pool += chars
        
        if self.config.include_special:
            chars = (
                self.SPECIAL_CHARS 
                if self.config.exclude_ambiguous 
                else self.SPECIAL_CHARS_FULL
            )
            pool += chars
        
        return pool
    
    def _get_required_chars(self) -> list[str]:
        """
        Obtenir au moins un caractère de chaque catégorie requise.
        
        Returns:
            Liste de caractères garantis dans le mot de passe
        """
        required = []
        
        if self.config.include_lowercase:
            chars = string.ascii_lowercase
            if self.config.exclude_ambiguous:
                chars = "".join(c for c in chars if c not in self.AMBIGUOUS_CHARS)
            required.append(secrets.choice(chars))
        
        if self.config.include_uppercase:
            chars = string.ascii_uppercase
            if self.config.exclude_ambiguous:
                chars = "".join(c for c in chars if c not in self.AMBIGUOUS_CHARS)
            required.append(secrets.choice(chars))
        
        if self.config.include_digits:
            chars = string.digits
            if self.config.exclude_ambiguous:
                chars = "".join(c for c in chars if c not in self.AMBIGUOUS_CHARS)
            required.append(secrets.choice(chars))
        
        if self.config.include_special:
            chars = (
                self.SPECIAL_CHARS 
                if self.config.exclude_ambiguous 
                else self.SPECIAL_CHARS_FULL
            )
            required.append(secrets.choice(chars))
        
        return required
    
    def generate(self) -> str:
        """
        Générer un mot de passe sécurisé.
        
        Returns:
            Mot de passe généré
        """
        pool = self._build_character_pool()
        required_chars = self._get_required_chars()
        
        # Générer les caractères restants
        remaining_length = self.config.length - len(required_chars)
        password_chars = required_chars + [
            secrets.choice(pool) for _ in range(remaining_length)
        ]
        
        # Mélanger de manière sécurisée
        secrets_list = password_chars
        for i in range(len(secrets_list) - 1, 0, -1):
            j = secrets.randbelow(i + 1)
            secrets_list[i], secrets_list[j] = secrets_list[j], secrets_list[i]
        
        return "".join(secrets_list)


def interactive_mode() -> None:
    """Mode interactif pour configurer et générer un mot de passe."""
    
    print("\n" + "="*60)
    print("🔐 GÉNÉRATEUR DE MOT DE PASSE SÉCURISÉ 🔐")
    print("="*60)
    
    try:
        # Longueur
        while True:
            try:
                length = int(
                    input("\n📏 Longueur du mot de passe (minimum 12) [16]: ") or "16"
                )
                if length < 12:
                    print("⚠️  La longueur doit être au minimum 12 caractères.")
                    continue
                break
            except ValueError:
                print("❌ Veuillez entrer un nombre valide.")
        
        # Options
        print("\n✅ Inclure dans le mot de passe :")
        include_uppercase = (
            input("  • Majuscules (A-Z) ? [O/n]: ").lower() != "n"
        )
        include_lowercase = (
            input("  • Minuscules (a-z) ? [O/n]: ").lower() != "n"
        )
        include_digits = (
            input("  • Chiffres (0-9) ? [O/n]: ").lower() != "n"
        )
        include_special = (
            input("  • Caractères spéciaux (!@#...) ? [O/n]: ").lower() != "n"
        )
        exclude_ambiguous = (
            input("\n🎯 Exclure les caractères ambigus (i, l, 1, O, 0) ? [O/n]: ").lower() != "n"
        )
        
        # Créer la configuration
        config = PasswordConfig(
            length=length,
            include_uppercase=include_uppercase,
            include_lowercase=include_lowercase,
            include_digits=include_digits,
            include_special=include_special,
            exclude_ambiguous=exclude_ambiguous,
        )
        
        # Générer
        generator = PasswordGenerator(config)
        password = generator.generate()
        
        # Afficher le résultat
        print("\n" + "="*60)
        print("✨ MOT DE PASSE GÉNÉRÉ AVEC SUCCÈS ✨")
        print("="*60)
        print(f"\n🔑 {password}\n")
        print("="*60)
        print("⚠️  IMPORTANT :")
        print("  • Conservez ce mot de passe dans un gestionnaire sécurisé")
        print("  • Ne le partagez jamais par email ou message")
        print("  • Modifiez-le régulièrement")
        print("="*60 + "\n")
        
    except ValueError as e:
        print(f"\n❌ Erreur de configuration : {e}")
        return


def main() -> None:
    """Fonction principale."""
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        interactive_mode()
    else:
        # Mode script - génération simple
        config = PasswordConfig(length=16)
        generator = PasswordGenerator(config)
        password = generator.generate()
        
        print("\n" + "="*60)
        print("🔒 MOT DE PASSE GÉNÉRÉ 🔒")
        print("="*60)
        print(f"\n{password}\n")
        print("="*60 + "\n")


if __name__ == "__main__":
    main()
