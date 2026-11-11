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
      color: "#2F4A3A;",
      fontFamily: "sans-serif",
      fontSize: "16px",
      "::placeholder": { color: "#FBF8F4" },
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

    stripe
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
      })
      .catch(function () {
        showPaymentError(
          "Something went wrong. Please check before trying again."
        );
      });
  });
})();
