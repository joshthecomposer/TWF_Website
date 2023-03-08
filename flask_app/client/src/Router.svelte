<script>
    import page from "page.js";
    import { setContext } from "svelte";

    function navigate(ctx, next) {
        console.log("Navigating to: " + ctx.path);
    }
    page("/about", navigate);
    page("*", () => console.log("Not found"));
</script>

<slot />