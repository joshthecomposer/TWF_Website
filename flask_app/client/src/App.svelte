<script>
	import { Router, Route} from "svelte-navigator";
	import Navbar from "./Nav.svelte";
	import Player from "./Episodes.svelte";
	import About from "./About.svelte";
	import Home from "./Home.svelte";
</script>

<Router primary={false}>
	<header>
		<Navbar />
	</header>
<main>
		<Route path="/">
			<Home />
		</Route>
		<Route path="about" >
			<About />
		</Route>
		
		<Route path="episodes">
			<Player />
		</Route>

		<Route path="merch">
			<h1>Merch</h1>
		</Route>
		<Route path="blog">
			<h1>Blog</h1>
		</Route>
		<Route path="subscribe">
			<h1>Subcsribe</h1>
		</Route>
		<Route path="contact">
			<h1>Contact</h1>
		</Route>
	</main>
</Router>

<style>
	main {
		height: 100%;
	}
</style>
