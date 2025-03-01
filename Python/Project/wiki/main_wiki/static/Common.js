$("body").prepend(`
	<nav class="navbar fixed-top">
	<ul class="menu d-flex justify-content-center">
		<li class="menu__item">
			<a href="../../">
				JATM Вики
			</a>
		</li>

		<li class="menu__item">
			<a href="../../account">
				Логин
			</a>
		</li>

		<li class="menu__item">
			<a href="../../account">
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