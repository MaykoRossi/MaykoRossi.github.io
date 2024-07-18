<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $to = "maykorossi@hotmail.com"; // Substitua pelo e-mail desejado
    $subject = "Novo formulário enviado - Pesquisa"; // Assunto específico para facilitar a filtragem
    
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $age = htmlspecialchars($_POST['age']);
    $dropdown = htmlspecialchars($_POST['dropdown']);
    $options = htmlspecialchars($_POST['options']);
    $preferences = isset($_POST['preferences']) ? implode(", ", $_POST['preferences']) : "Nenhuma preferência selecionada";
    $comments = htmlspecialchars($_POST['comments']);
    
    $message = "
    Nome: $name\n
    E-mail: $email\n
    Idade: $age\n
    Opção: $dropdown\n
    Opção Escolhida: $options\n
    Preferências: $preferences\n
    Comentários: $comments
    ";
    
    $headers = "From: $email" . "\r\n" .
               "Reply-To: $email" . "\r\n" .
               "X-Mailer: PHP/" . phpversion();
    
    if (mail($to, $subject, $message, $headers)) {
        echo "E-mail enviado com sucesso!";
    } else {
        echo "Falha ao enviar e-mail.";
    }
} else {
    echo "Método de requisição inválido.";
}
?>