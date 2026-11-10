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
      color: "#000",
      fontFamily: "sans-serif",
      fontSize: "16px",
      "::placeholder": { color: "#aab7c4" },
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

  // After selecting place order:
  const form = document.getElementById("payment-form");
  const submitButton = document.getElementById("submit-button");

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    card.update({ disabled: true });
    submitButton.disabled = true;

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
          // Payment failed:
          errorDiv.textContent = result.error.message;
          card.update({ disabled: false });
          submitButton.disabled = false;
        } else if (result.paymentIntent.status === "succeeded") {
          // Payment worked:
          form.submit();
        }
      });
  });
})();
