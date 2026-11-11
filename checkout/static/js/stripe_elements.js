(function () {
  "use strict";

  // From django variables
  const stripePublicKey = JSON.parse(
    document.getElementById("id_stripe_public_key").textContent
  );
  const clientSecret = JSON.parse(
    document.getElementById("id_client_secret").textContent
  );

  // Start Stripe and create the card box
  const stripe = Stripe(stripePublicKey);
  const elements = stripe.elements();

  const style = {
    base: {
      color: "#2F4A3A",
      fontFamily: "sans-serif",
      fontSize: "16px",
      "::placeholder": { color: "gray" },
    },
    invalid: { color: "#dc3545", iconColor: "#dc3545" },
  };

  const card = elements.create("card", { style: style });
  card.mount("#card-element");

  // Show card errors
  const errorDiv = document.getElementById("card-errors");

  card.addEventListener("change", function (event) {
    errorDiv.textContent = event.error ? event.error.message : "";
  });

  const form = document.getElementById("payment-form");
  const submitButton = document.getElementById("submit-button");
  const loadingOverlay = document.getElementById("loading-overlay");

  // Overlay logic
  const MIN_OVERLAY_MS = 1500;
  let overlayShownAt = 0;

  function showOverlay() {
    overlayShownAt = Date.now();
    loadingOverlay.classList.add("is-visible");
  }

  function hideOverlay(afterHidden) {
    const elapsed = Date.now() - overlayShownAt;
    const remaining = Math.max(0, MIN_OVERLAY_MS - elapsed);

    setTimeout(function () {
      loadingOverlay.classList.remove("is-visible");
      if (afterHidden) afterHidden();
    }, remaining);
  }

  const saveInfoBox = document.getElementById("id-save-info");

  function cacheCheckoutData() {
    const data = new FormData(form);   // all the form fields plus the CSRF token
    data.set("client_secret", clientSecret);
    data.set("save_info", saveInfoBox && saveInfoBox.checked ? "1" : "0");
    return fetch(form.dataset.cacheUrl, { method: "POST", body: data });
  }

  // Show an error and let the user try again
  function showPaymentError(message) {
    hideOverlay(function () {
      errorDiv.textContent = message;
      errorDiv.scrollIntoView({ behavior: "smooth", block: "center" });
      card.update({ disabled: false });
      submitButton.disabled = false;
    });
  }

  // After selecting place order:
  form.addEventListener("submit", function (event) {
    event.preventDefault();
    card.update({ disabled: true });
    submitButton.disabled = true;
    errorDiv.textContent = "";
    showOverlay();

    cacheCheckoutData()
      .then(function (response) {
        if (!response.ok) {
          showPaymentError(
            "Sorry, we couldn't begin your payment. Your card has not been charged. Please try again."
          );
          return;
        }

        return stripe
          .confirmCardPayment(clientSecret, {
            payment_method: {
              card: card,
              billing_details: {
                name: form.elements["full_name"].value.trim(),
                email: form.elements["email"].value.trim(),
                phone: form.elements["phone_number"].value.trim(),
              },
            },
          })
          .then(function (result) {
            if (result.error) {
              showPaymentError(result.error.message);
            } else if (result.paymentIntent.status === "succeeded") {
              form.submit();
            } else {
              showPaymentError(
                "Your payment hasn't completed yet. Please check before trying again."
              );
            }
          });
      })
      .catch(function () {
        showPaymentError("Something went wrong. Please check before trying again.");
      });
  });
})();
