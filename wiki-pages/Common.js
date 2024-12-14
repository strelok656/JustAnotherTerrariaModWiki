$("head").prepend(`
	<!-- Google Fonts -->
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@100..900&display=swap" rel="stylesheet">

	<!-- Bootstrap -->
	<link rel="stylesheet" type="text/css" href="../Libraries/bootstrap.min.css">
	<script type="text/javascript" src="../Libraries/bootstrap.bundle.min.js"></script>

	<!-- Styles-->
	<link rel="stylesheet" type="text/css" href="../css/Common.css">
	<link rel="stylesheet" type="text/css" href="../css/Footer.css">
	<link rel="stylesheet" type="text/css" href="../css/WikiPages.css">
	<link rel="stylesheet" type="text/css" href="../css/NavBar.css">

	<!-- Favicon -->
	<link rel="icon" href="../img/SiteIcon.png">
`)

$("body").prepend(`
	<nav class="navbar fixed-top">
	<ul class="menu d-flex justify-content-center">
		<li class="menu__item">
			<a href="../index.html">
				JATM Вики
			</a>
		</li>

		<li class="menu__item">
			<a href="#">
				Логин
			</a>
		</li>

		<li class="menu__item">
			<a href="#">
				Создать аккаунт
			</a>
		</li>

		<li class="menu__item">
			<input type="text" placeholder="Поиск">
		</li>
	</ul>
</nav>


`)

$("body").append(`
	<footer>
	<div class="container">
		<div class="row">
			<div class="col-lg-12">
				<div class="footer-info">
					Алмаз Г.
					<br>
					2024
					<br>
					Макет сайта на кружок Программисты
				</div>
			</div>
		</div>
	</div>
</footer>
	`)