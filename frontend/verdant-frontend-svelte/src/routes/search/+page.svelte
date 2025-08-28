<script lang="ts">
  import { query } from "$app/server";
  import { page } from "$app/stores";
  import { onMount } from "svelte";
  import type { PageLoad } from "./$types";

  const searchQueries = $derived($page.url.searchParams.get("term") || "");
  const queryList = searchQueries.split(" ");

  let matchScore = $state(0);
  let websitesLoaded = $state(0);
  let websites = $state([]);

  let loading = $state(true);
  let items = $state([]);
  let inputValue = $state(searchQueries);

  const date = new Date();
  const formattedDate = date.toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });

  async function getSites(searchTerms: string[]) {
    try {
      const params = new URLSearchParams();
      searchTerms.forEach((term) => {
        if (term.trim()) {
          params.append("term", term.trim());
        }
      });

      const res = await fetch(
        `https://verdant-backend-production.up.railway.app/verdant/api?${params}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      if (!res.ok) {
        const resError = `Failed to fetch items! ${res.status}`;
        console.error(resError);
        return { items: [], error: resError };
      }
      items = await res.json();
    } catch (error) {
      console.log(error);
      // TODO: Add an error component and set it to "true" similar to loading component
    } finally {
      loading = false;
      console.log(items);
      matchScore = items.match_score || 0;
      websitesLoaded = items.websites_loaded || 0;
      websites = items.websites || [];
    }
  }

  function limitURL(url: string) {
    if (url.length > 80) {
      let output = url.slice(0, 80) + "...";
      return output;
    } else {
      return url;
    }
  }

  function handleKeyDown(event: { key: string }) {
    if (event.key === "Enter") {
      const inputQuery = inputValue.split(" ");
      getSites(inputQuery); // new fetch req with new value from search bar;
    }
  }

  onMount(() => {
    if (queryList.length > 0) {
      getSites(queryList);
    }

    const handleGlobalKeyDown = (event: { key: string }) => {
      const activeElement = document.activeElement;
      if (activeElement && activeElement.id === "search-page-bar") {
        handleKeyDown(event);
      }
    };
    window.addEventListener("keydown", handleGlobalKeyDown);
    return () => window.removeEventListener("keydown", handleGlobalKeyDown);
  });
</script>

<div style="display: flex;">
  <div id="searchpage">
    <h1 id="search-top-text" class="verdant-text">Verdant</h1>
    <input
      name="search"
      class="search-bar"
      id="search-page-bar"
      autocomplete="off"
      placeholder={searchQueries}
      bind:value={inputValue}
    />

    {#if loading}
      <div id="loading-box">
        <h2 style="font-size: 36px; color: #003106;">Loading...</h2>
        <div id="outer-bar">
          <div id="inner-bar"></div>
        </div>
        <div style="width: 350px; display: flex; align-self: center;">
          <h2 style="font-size: 32px; color: #003106;">
            Note: First time searches may take 10-20s to load
          </h2>
        </div>
      </div>
    {/if}

    {#if !loading}
      <div id="results-container">
        <div
          id="percent-match-box-small"
          class="result-box"
          style="height: 142px; max-width: 570px;"
        >
          <div id="percent-elements-small">
            <h2 id="percent-match-text" style="color: #003106;">
              Percent Match:
            </h2>
            <div id="percent-bar-container-small">
              <h2 style="font-size: 64px; color: #135902; margin-top: 10px;">
                {Math.round(matchScore)}%
              </h2>
              <div
                id="outer-percent-bar-small"
                style="display: flex; align-items: center;"
              >
                <div
                  id="inner-percent-bar-small"
                  style="height: {matchScore}%"
                ></div>
              </div>
            </div>
          </div>

          <div
            id="percent-green-bar-small"
            class="green-bar"
            style="height: 100%; width: 3px; background-color: rgba(45, 88, 57, 0.5); margin-top: 0px; margin-left: 40px; margin-right: 40px; border-radius: 999px;"
          ></div>
          <div id="websites-loaded-small" style="margin-top: 0.7px;">
            <h2 id="websites-loaded-text-small" style="color: #003106;">
              Websites Loaded:
            </h2>
            <h2
              id="websites-loaded-fraction-small"
              style="font-size: 64px; color: #585858; margin-top: 23px; margin-left: 23px;"
            >
              {websitesLoaded}/10
            </h2>
          </div>
        </div>
        {#each websites as site}
          <div class="result-box">
            <div class="title-bar">
              <div class="verdant-logo"><h1 class="v-text">V</h1></div>
              <div class="url-box">
                <h2 style="font-family: Roboto Flex;">{site.title}</h2>
                <h3
                  style="font-family: Roboto Flex; margin-top: 1.5px; color: #797979;"
                >
                  {limitURL(site.url)}
                </h3>
              </div>
            </div>
            <a href={site.url}>
              <h1 class="url-text">{site.title}</h1>
            </a>
            <h2 class="description-text">
              <span class="date-text">{formattedDate} - </span>
              {site.description}
            </h2>
          </div>
        {/each}
      </div>
    {/if}
  </div>

  {#if !loading}
    <div
      id="percent-match-box"
      class="result-box"
      style="width: 390px; height: 278px; margin-top: 141px; margin-left: 34px; margin-right: 34px;"
    >
      <h2 style="font-size: 40px;">Percent Match:</h2>
      <div id="percent-elements">
        <h2 style="font-size: 128px; color: #135902;">
          {Math.round(matchScore)}%
        </h2>
        <div id="outer-percent-bar" style="display: flex; align-items: center;">
          <div id="inner-percent-bar" style="height: {matchScore}%"></div>
        </div>
      </div>
      <div
        id="percent-green-bar"
        class="green-bar"
        style="width: 100%; align-self: center; height: 3px; background-color: rgba(45, 88, 57, 0.5); margin-top: 20px;"
      ></div>
      <h2 style="margin-top: 20px; font-size: 36px; color: #929292;">
        Websites Loaded: <span
          style="font-size: 46px; color: #585858; margin-left: 10px;"
        >
          {websitesLoaded}
          /10</span
        >
      </h2>
    </div>
  {/if}
</div>
