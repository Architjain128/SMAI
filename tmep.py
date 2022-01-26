plt.subplots_adjust(left=1.5, bottom=1.5, right=2, top=2, wspace=1, hspace=1)
plt.figure(figsize=(12,8))
plt.subplot(2, 2, 1)
plt.plot(ham_k_val_t,ham_acc_t)
plt.title('Accuracy')

plt.subplot(2, 2, 2)
plt.plot(ham_k_val_t,ham_f1_t)
plt.title('F1-score')

plt.subplot(2, 2, 3)
plt.plot(ham_k_val_t,ham_re_t)
plt.title('Recall')

plt.subplot(2, 2, 4)
plt.plot(ham_k_val_t,ham_pr_t)
plt.title('Precision')

plt.suptitle("hamine Similarity")
plt.show()