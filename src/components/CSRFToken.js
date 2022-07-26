export async function getCsrfToken() {

    const response = await fetch("/api/csrf/", {
      credentials: 'include',
    });
    const data = await response.json();
    return data.csrfToken;
}