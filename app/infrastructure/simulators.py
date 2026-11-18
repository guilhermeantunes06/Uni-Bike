"""Adaptadores e simuladores de sistemas externos (IoT MQTT / SSO Institucional)."""


class IoTLockSimulator:
    """Simulador do módulo IoT da e-bike para desbloqueio/bloqueio remoto."""

    def send_unlock_command(self, ebike_id: str) -> bool:
        """Simula o envio do comando de desbloqueio por MQTT/TLS e confirmação da tranca."""
        return bool(ebike_id)


class SSOSimulator:
    """Simulador do fornecedor de identidade institucional (OAuth2 / OIDC)."""

    def validate_token(self, email: str) -> dict[str, str]:
        """Simula a validação federada do utilizador pelo email institucional."""
        domain = email.split("@")[-1] if "@" in email else ""
        return {"email": email, "domain": domain}
