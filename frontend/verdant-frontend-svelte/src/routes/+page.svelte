<script lang="ts">
  import { goto } from "$app/navigation";
  import { onMount } from "svelte";
  import randomQueries from "$lib/randomList";

  let searchQuery = "";

  function sendQuery() {
    const spaceCheck = searchQuery.replace(/\s/g, ""); // removes all spaces from queries

    if (spaceCheck.length > 0) {
      goto(`/search?term=${encodeURIComponent(searchQuery)}`);
    }
  }

  function sendRandomQuery() {
    const randomItem =
      randomQueries[Math.floor(Math.random() * randomQueries.length)];

    goto(`/search?term=${encodeURIComponent(randomItem)}`);
  }

  function handleKeyDown(event: { key: string }) {
    if (event.key === "Enter") {
      sendQuery();
    }
  }

  onMount(() => {
    const handleGlobalKeyDown = (event: { key: string }) => {
      const activeElement = document.activeElement;
      if (activeElement && activeElement.id === "home-page-bar") {
        handleKeyDown(event);
      }
    };
    window.addEventListener("keydown", handleGlobalKeyDown);
    return () => window.removeEventListener("keydown", handleGlobalKeyDown);
  });
</script>

<div id="search-content">
  <div id="logo">
    <h1 class="verdant-text">Verdant</h1>
    <p>adj: green in tint or color</p>
  </div>

  <input
    bind:value={searchQuery}
    id="home-page-bar"
    name="search"
    class="search-bar"
    autocomplete="off"
  />

  <div id="buttons">
    <div class="glass-button-green" on:click={sendQuery}>
      <h2>Search</h2>
    </div>
    <div class="glass-button-green" on:click={sendRandomQuery}>
      <h2>Random</h2>
    </div>
  </div>
</div>
