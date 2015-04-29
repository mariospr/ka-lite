//Models

window.ContentResumeModel = Backbone.Model.extend({
	defaults: {
		lesson_title: "",
		lesson_description: "blahblah"
	},

	initialize: function() {
        //this.channel = options.channel;
        console.log(this.get('lesson_description'));
    }
});

window.SuggestedContentModel = Backbone.Model.extend({
	defaults: {
		interest_topic: "interest topic",
		lesson_title: "lesson title",
		lesson_description: "lesson description",
		suggested_topic_title: "suggested topic",
		suggested_topic_description: "topic description"
	},

	initialize: function() {

	}
});


//Collections

window.ContentNextStepsCollection = Backbone.Collection.extend({
	model: SuggestedContentModel
});

window.ContentExploreCollection = Backbone.Collection.extend({
	model: SuggestedContentModel
});