$(document).ready(function () {
    if (typeof searchUrl === "undefined") {
        console.error(
            "searchUrl is not defined. Make sure it's set in home.html.",
        );
        return;
    }
    $("#search").on("keyup", function () {
        let query = $(this).val().trim();
        let currentUrl = new URL(window.location.href);
        let tableId = currentUrl.searchParams.get("table_id");
        $.ajax({
            url: searchUrl,
            data: { q: query, table_id: tableId },
            dataType: "json",
            success: function (response) {
                let rowsHtml = response.items.length
                    ? ""
                    : `<tr id="no-results"><td colspan="5" class="py-3 text-center text-zinc-400">No results found</td></tr>`;

                $.each(response.items, function (index, item) {
                    rowsHtml += `
                        <tr class="border-t text-center dark:border-zinc-800">
                    <td
                        class="rounded-lg py-3 transition duration-300 hover:bg-zinc-900"
                    >
                        ${item.id}
                    </td>
                    <td
                        class="rounded-lg py-3 transition duration-300 hover:bg-zinc-900"
                    >
                        ${item.name}
                    </td>
                    <td
                        class="rounded-lg py-3 transition duration-300 hover:bg-zinc-900"
                    >
                    ${item.price}
                    </td>
                    <td class="w-28 py-3">
                        <a href="items/${item.id}/edit/">
                            <button
                                class="w-20 cursor-pointer rounded-lg border border-zinc-800 p-px transition duration-300 hover:bg-zinc-900"
                            >
                                edit
                            </button>
                        </a>
                    </td>
                    <td class="w-28 py-3">
                        <a href="items/${item.id}/delete/">
                            <button
                                class="w-20 cursor-pointer rounded-lg border border-zinc-800 p-px transition duration-300 hover:bg-zinc-900"
                            >
                                delete
                            </button>
                        </a>
                    </td>
                </tr>
                    `;
                });

                $("#items-table").html(rowsHtml);
            },
        });
    });
});
