<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
	import "../app.css"
	import { page } from '$app/stores';
	import homeIcon from '../lib/assets/homeIcon.png';
	import bookIcon from '../lib/assets/bookIcon.png';
	import bookMarkIcon from '../lib/assets/bookMarkIcon.png';

	let { children } = $props();

	let sidebarOpen = $state(false);

	function toggleSidebar() {
		sidebarOpen = !sidebarOpen;
	}
	function closeSidebar() {
		sidebarOpen = false;
	}
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="background-gradient"></div>
<div id="main" on:click={closeSidebar}>

	<div id="hamburger-icon" on:click|stopPropagation={toggleSidebar} style="display: {sidebarOpen ? 'none' : ''}">
		<div class="hamburger-icon-row"></div>
		<div class="hamburger-icon-row"></div>
		<div class="hamburger-icon-row"></div>
	</div>

		<div id="sidebar" class:open={sidebarOpen}>

			<div id="sidebar-text">
				<div id="circle"></div>
				<h1 id="V">V</h1>
			</div>

			<div id="sidebar-buttons">
				<a href="/">
					<div class="sidebar-button">
						<div id="home-button" class={$page.url.pathname == "/" || $page.url.pathname == "/search" ? 'glass-button-green' : 'glass-button'}><img src={homeIcon} style="transform: scale(0.09);"></div>
						<h2 class={$page.url.pathname == "/" || $page.url.pathname == "/search" ? 'glass-button-green-text' : ''}>Home</h2>
					</div>
				</a>
				<a href="/about">
					<div class="sidebar-button">
						<div id="search-button" class={$page.url.pathname == "/about" ? 'glass-button-green' : 'glass-button'}><img src={bookIcon} style="transform: scale(0.09);"><h2></h2></div>
						<h2 class={$page.url.pathname == "/about" ? 'glass-button-green-text' : ''}>About</h2>
					</div>
				</a>
				<a href="/directory">
					<div class="sidebar-button">
						<div id="directory-button" class={$page.url.pathname == "/directory" ? 'glass-button-green' : 'glass-button'}><img src={bookMarkIcon} style="transform: scale(0.1);"></div>
						<h2 class={$page.url.pathname == "/directory" ? 'glass-button-green-text' : ''}>Directory</h2>
					</div>
				</a>
			</div>
		</div>
	<div id={$page.url.pathname == "/" ? "homepage" : ""}>
		{@render children?.()} <!--Renders currently loaded page-->
	</div>
</div>

