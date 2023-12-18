What is Remix?
    A React Framework that builds on top of React.js (still writing React code)

Why Remix?
    Blend server-side + client-side code into the same file. 
        - Pattern known as "co-location", where related code is placed together
        - Better organization and understanding how FE + BE interacts
        -

Remix vs Next.js


Remix
    Always server-side rendered.
    Always needs a host to support server side code execution


Next.js
    Pre-renders static pages at build time. Can also SSR
    Only need a static host (capable of server side code execution)


    
```Server-Side Rendering (SSR):
    Technique where server generates the HTML for a page and sends it to the client
    Executes code to fetch data / perform operations before sending fully rendered HTML to client
    Helps with Search Engine Optimization (SEO)
        - Gives Search engines immediately available content for indexing
        - I.e. User Searches for Cooking Recipe:

            The user enters a search query for a cooking recipe into a search engine.
            Search Engine Crawls and Indexes Content:

            The search engine crawls the web and indexes pages based on their content.
            Client-Side Rendered Page:

            If the cooking recipe website relies on client-side rendering (CSR), the initial HTML page may not contain the actual recipes. Instead, it might have JavaScript code that fetches and renders the recipes after the page loads.
            Search Engine Crawlers May Miss Content:

            Search engine crawlers may not execute JavaScript or wait for client-side rendering to complete. As a result, they might miss the actual recipes during the crawling process.
            SEO Impact:

            The cooking recipes might not be appropriately indexed, impacting the website's visibility in search results when users look for specific recipes.
    Faster initial page loads
        - CSR browser needs to wait for JS to execute and fetch data before rendering. 
        - Critical content is in initial HTML payload. Improves perceived performance.
        - Avoids Flash of Empty Content (users see empty page before client-side rendering completes)

Client-Side Rendering (CSR):
    Browser fetches JS and renders page on client side```

    