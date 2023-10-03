<!DOCTYPE html>
<html>

<head>
    <title>Listar Produtos</title>
</head>

<body>

<h1>Listar Produtos</h1>

<table>
    <tr>
        <th>Nome</th>
        <th>Id</th>
        <th>QTD</th>
        <th>Valor</th>
        <th>Ação</th>
    </tr>

    <?php
    $arqProduto = fopen("Produtos.txt", "r") or die("Erro ao abrir arquivo");
    $total = 0;

    while (!feof($arqProduto)) {
        $linha = fgets($arqProduto);
        $colunaDados = explode(";", $linha);
        $nome = $colunaDados[0];
        $ID = $colunaDados[1];
        $QTD = $colunaDados[2];
        $valor = $colunaDados[3];

        echo "<tr>";
        echo "<td>". $nome . "</td>";
        echo "<td>". $ID . "</td>";
        echo "<td>". $QTD . "</td>";
        echo "<td>R$ ". number_format($valor, 2, ',', '.') . "</td>";
        echo '<td>';
        echo 'Quantidade: <input type="number" name="QTD_' . $ID . '" value="0">';
        echo '<br>';
        echo '<a href="adicionarproduto.php?ID=' . $ID . '">Adicionar</a>';
        echo '</td>';
        echo "</tr>";

        $total += $valor * $QTD;
    }

    fclose($arqProduto);
    ?>

</table>

<h2>Total do Carrinho: R$ <?php echo number_format($total, 2, ',', '.'); ?></h2>

</body>

</html>