# Users

Última atualização: Set. 12, 2025

---

---

## Descrição

Seção destinada ao gerenciamento dos usuários do sistema.

Divididas em “***All Users***” e “***Permissions***”.

<img src="$WRS_MODULE$/images/imported/shared/f742a7714da7b467.png" alt="image-20250912-201422.png"/>

---

## 1. All Users

Tela referente ao gerenciamento dos usuários cadastrados.

<img src="$WRS_MODULE$/images/imported/shared/f46285d87964ad72.png" alt="image-20250912-183644.png"/>

1. **Name:** Nome do usuário.
2. **email:** E-mail de contato profissional.
3. **User name:**Log-in do usuário no sistema.
4. **CreatedAt:**Data de criação do usuário no sistema.
5. **Ícone “**
  <img src="$WRS_MODULE$/images/imported/shared/f5110603dc5e9077.png" alt="image-20250911-183944.png"/>
  **”:**Ao clicar, será exibida a tela de cadastro abaixo, contendo os campos:
  1. **Name:** Nome do usuário.
  2. **userName:** Log-in do usuário no sistema.
  3. **email:** E-mail de contato profissional.
  4. **password:** Senha criada para o usuário.
  5. [**owners**](br-management.md#1-7-owner)**:**  Separador de informações entre os usuários. Somente os usuários vinculados a um *owner* específico terão acesso às informações correspondentes.
  6. **countries:** País de acesso ao usuário cadastrado.
  7. **orderscreenTheaters:**Campo específico para usuários que irão utilizar a função de *orderscreen*.
  8. **Theaters:** Cinema do usuário. Essa função só será utilizada se o Role do usuário for GO (Gerente Operacional, possui acesso a mais de um cinema)
  9. **roles:**Item que determina o nível do usuário dentro do sistema. Ele determinará as telas em que o usuário terá acesso e também o que ele poderá fazer dentro do Communique.
  10. **Support Leader:**Determina se o usuário é o Líder de suporte, habilitando a função de envio de e-mail na tela inicial do dashboard - parte superior.
6. **Ícone “SAVE”:**Salva as informações e cria um novo usuário.

<img src="$WRS_MODULE$/images/imported/shared/06b44b708aa75d1e.png" alt="image-20250912-191807.png"/>

---

## 2. Permissions

Lista de *roles* disponíveis no sistema. As permissões são gerenciadas diretamente no banco de dados e definem os níveis de acesso dos usuários.

<img src="$WRS_MODULE$/images/imported/shared/735f4de35f4eadd8.png" alt="image-20250912-192216.png"/>
