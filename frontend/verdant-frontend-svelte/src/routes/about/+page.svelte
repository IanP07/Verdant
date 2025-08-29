<script lang="ts">
  import Figma from "../../lib/assets/tech-icons/Figma.png";
  import Flask from "../../lib/assets/tech-icons/Flask.png.webp";
  import MongoDB from "../../lib/assets/tech-icons/MongoDB.png";
  import Python from "../../lib/assets/tech-icons/Python.png";
  import Scrapy from "../../lib/assets/tech-icons/Scrapy.png";
  import Svelte from "../../lib/assets/tech-icons/Svelte.png";
  import Typescript from "../../lib/assets/tech-icons/Typescript.png";
</script>

<div id="homepage-about">
  <div id="about-main">
    <div id="about-us-header-div"><h1>About Verdant</h1></div>
    <div id="about-us-text-div">
      <h2>
        Verdant is a minimalist, full-stack search engine that indexes ~25k
        pages, stored in a JSON-based database.
      </h2>
      <h2 style="margin-top: 50px;">
        It focuses on technology and educational websites, offering a clean,
        lightweight search experience.
      </h2>
    </div>
    <div id="tech-stack-wrapper">
      <div
        id="frontend-wrapper"
        style="display: flex; flex-direction: column; align-items: center;"
      >
        <h1 style="font-size: 36px; margin-bottom: 5px;">Frontend</h1>
        <div style="display: flex; gap: 25px;">
          <div class="tech-bubble">
            <img src={Figma} style="height: 80px;" />
          </div>
          <div class="tech-bubble">
            <img src={Svelte} style="height: 80px;" />
          </div>
        </div>
        <div
          id="third-frontend-bubble"
          class="tech-bubble"
          style="margin-top: 20px;"
        >
          <img src={Typescript} style="height: 80px;" />
        </div>
      </div>
      <div class="tech-stack-divider"></div>

      <div
        id="backend-wrapper"
        style="display: flex; flex-direction: column; align-items: center;"
      >
        <h1 style="font-size: 36px; margin-bottom: 5px;">Backend</h1>
        <div class="tech-bubble-wrapper">
          <div class="tech-bubble">
            <img src={MongoDB} style="height: 80px;" />
          </div>
          <div class="tech-bubble" style="margin-top: 20px;">
            <img src={Flask} style="height: 80px;" />
          </div>
        </div>
      </div>

      <div class="tech-stack-divider"></div>

      <div
        id="crawler-wrapper"
        style="display: flex; flex-direction: column; align-items: center;"
      >
        <h1 style="font-size: 36px; margin-bottom: 5px;">Crawler</h1>
        <div class="tech-bubble-wrapper">
          <div class="tech-bubble">
            <img src={Scrapy} style="height: 80px;" />
          </div>
          <div class="tech-bubble" style="margin-top: 20px;">
            <img src={Python} style="height: 80px;" />
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
`
