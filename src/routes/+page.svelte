<script>
	let url = $state('');
	let contentReturned = $state(null);
	let error = $state(null);
	let loading = $state(false);

	const webScrape = async () => {
		let res = await fetch('http://localhost:8000/webscrape', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				url
			})
		});
		let data = await res.json();
        let content = data.content

        let fetchedContentContainer = document.getElementById('fetchedContent')
		if (data.success) {
			fetchedContentContainer.innerHTML = content;
			error = null;
		} else {
			fetchedContentContainer.innerHTML = null;
			error = data.error;
		}
		console.log('Data: ', data);
        console.log(document.getElementById('fetchedContent'))
        
	};
</script>

<div class="mx-auto w-5/6 space-y-4 py-40">
	<p class="text-3xl text-black">
		This is <span class="font-bold">WebScrapy</span>
	</p>
	<p class="text-base text-gray-700">
		Enter a URL <span class="italic">(with the <span class="font-semibold">"https://"</span>)</span> in
		the input and click submit to see what you can do
	</p>
	<form
		onsubmit={async (e) => {
			e.preventDefault();
			loading = true;
			await webScrape();
			url = '';
			loading = false;
		}}
		class="space-y-4"
	>
		<div
			class="animated flex w-full gap-x-1 rounded px-2 py-2 lowercase outline-2 outline-gray-200 outline-dashed has-[input:focus-within]:outline-black has-[input:focus-within]:outline-solid has-[input:hover]:outline-black"
		>
			<input
				placeholder="https://www.ncregister.com/"
				class="w-full font-semibold placeholder-gray-200 outline-none placeholder:font-normal"
				bind:value={url}
				oninput={() => {
					url = url.replaceAll(/\s+/g, '');
				}}
				type="url"
			/>
		</div>
		<button
			class="animated cursor-pointer rounded bg-gray-100 px-4 py-2 text-black hover:bg-gray-200"
			type="submit"
		>
			Go!
		</button>
	</form>
	{#if loading == true}
    <div class="flex gap-x-1">
        <p class="text-black font-bold animate-bounce">
            .
        </p>
        <p class="text-black font-bold animate-bounce delay-75 transition">
            .
        </p>
        <p class="text-black font-bold animate-bounce delay-150 transition">
            .
        </p>
        <p class="text-black font-bold animate-bounce delay-200 transition">
            .
        </p>
    </div>
    {/if}
	{#if error}
		<p class="text-rose-400 italic">
			{error}
		</p>
	{/if}
		<div id="fetchedContent" class="h-80 w-full overflow-y-scroll text-wrap">
		</div>
</div>
