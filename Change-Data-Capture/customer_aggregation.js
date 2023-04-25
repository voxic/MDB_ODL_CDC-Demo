[
  {
    /**
     * specifications: The fields to
     *   include or exclude.
     */
    $project: {
      first_name: "$payload.after.customer_firstname",
      last_name: "$payload.after.customer_lastname",
      customer_id: "$payload.after.id",
    },
  },
  {
    /**
     * into: The target collection.
     * on: Fields to  identify.
     * let: Defined variables.
     * whenMatched: Action for matching docs.
     * whenNotMatched: Action for non-matching docs.
     */
    $merge: {
      into: "customers",
      on: "customer_id",
      whenMatched: "replace",
      whenNotMatched: "insert",
    },
  },
];
