<?php

include 'vendor/autoload.php';

$pdfFile = $_FILES['pdfFile'];
$pdfFilepath = "files/" . $pdfFile['name'];

move_uploaded_file($pdfFile['tmp_name'], $pdfFilepath);

$parser = new \Smalot\PdfParser\Parser();
$pdf = $parser->parseFile($pdfFilepath);
$text = $pdf->getText();

$splitStrings = explode("正本：", $text);
$original = "正本:" . explode("\n", $splitStrings[1])[0];


$obj = new stdClass();
$obj->original = $original;

echo json_encode($obj);

