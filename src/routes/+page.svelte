<script>
	let url = $state('');

	const webScrape = async () => {
		alert(`The url entered is ${"https://"+url}`);
        let data = await fetch("/webscrape", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url
            })
        })
	};
</script>

<div class="mx-auto w-5/6 space-y-4 py-40">
	<p class="text-3xl text-black">
		This is <span class="font-bold">WebScrapy</span>
	</p>
	<p class="text-base text-gray-700">
		Enter a URL <span class="italic">(without the "https://")</span> in the input and click submit to see what you can do
	</p>
	<form onsubmit={()=>{
        webScrape()
    }} class="space-y-4">
		<div
			class="animated mya flex w-full gap-x-1 rounded px-2 py-2 lowercase outline-2 outline-gray-200 outline-dashed has-[input:focus-within]:outline-black has-[input:focus-within]:outline-solid has-[input:hover]:outline-black"
		>
			<p class="text-gray-700">https://</p>
			<input
				placeholder="www.ncregister.com/"
				class="w-full font-semibold placeholder-gray-200 outline-none"
				bind:value={url}
				oninput={() => {
					url = url.replaceAll(/\s+/g, '');
                    url = url.replaceAll("https://", "")
				}}
				type="text"
			/>
		</div>
		<button
			class="animated cursor-pointer rounded bg-gray-100 px-4 py-2 text-black hover:bg-gray-200"
			type="submit"
		>
			Go!
		</button>
	</form>
</div>
